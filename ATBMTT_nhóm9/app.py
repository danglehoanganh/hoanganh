from flask import Flask, render_template, request, redirect, url_for, flash
import os
import subprocess

app = Flask(__name__)
app.secret_key = 'replace-with-your-secret'

# Ensure folders exist
os.makedirs('keys', exist_ok=True)
os.makedirs('parts', exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    output = ''
    if request.method == 'POST':
        action = request.form.get('action')
        try:
            # Run command and capture output
            cmd_map = {
                'generate_keys': ['python', 'generate_keys.py'],
                'create_assignment': ['python', 'create_assignment.py'],
                'encrypt_split': ['python', 'sender.py'],
                'decrypt_merge': ['python', 'receiver.py'],
            }
            cmd = cmd_map.get(action)
            if cmd:
                result = subprocess.run(cmd, capture_output=True, text=True)
                if result.returncode == 0:
                    flash(f"Action '{action}' completed successfully.")
                else:
                    flash(f"Action '{action}' failed with return code {result.returncode}.")
                output = result.stdout + '\n' + result.stderr
            else:
                flash(f"Unknown action: {action}")
        except Exception as e:
            flash(f'Error during {action}: {e}')
        return redirect(url_for('index'))

    # Determine statuses for template
    statuses = {
        'keys': os.path.exists('keys/public.pem') and os.path.exists('keys/private.pem'),
        'assignment': os.path.exists('assignment.txt'),
        'parts': any(os.path.exists(os.path.join('parts', f)) for f in os.listdir('parts')) if os.path.exists('parts') else False,
        'received': os.path.exists('assignment_received.txt'),
    }
    return render_template('index.html', output=output, statuses=statuses)

if __name__ == '__main__':
    app.run(debug=True)