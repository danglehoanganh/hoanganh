const chatWithAI = async (req, res) => {
  try {
    const { message, context } = req.body;
    console.log('Received message:', message);
    console.log('Context:', context);
    console.log('OPENAI_API_KEY set:', !!process.env.OPENAI_API_KEY);

    // Simple fallback for testing
    if (!message) {
      return res.json({ response: 'Xin chào! Tôi là chatbot trợ lý fitness.' });
    }

    // Use OpenAI
    const OpenAI = require('openai');
    const openai = new OpenAI({
      apiKey: process.env.OPENAI_API_KEY,
    });

    const systemPrompt = `
Bạn là chatbot trợ lý fitness chuyên nghiệp cho ứng dụng FitnessApp. Nhiệm vụ của bạn là hỗ trợ người dùng về các vấn đề liên quan đến tập luyện, sức khỏe, dinh dưỡng và lối sống lành mạnh.

Thông tin về ứng dụng:
- Ứng dụng giúp người dùng theo dõi BMI, đặt lịch tập luyện, gợi ý bài tập dựa trên BMI.
- Các tính năng chính: Đăng ký/đăng nhập, onboarding (nhập thông tin cá nhân), trang profile (xem thống kê BMI, gợi ý bài tập, đặt lịch), trang progress (theo dõi tiến độ).

Hướng dẫn trả lời:
- Luôn trả lời bằng tiếng Việt.
- Giữ giọng điệu thân thiện, khuyến khích và chuyên nghiệp.
- Nếu người dùng hỏi về BMI: Giải thích BMI là gì, cách tính, và các mức độ (thiếu cân <18.5, bình thường 18.5-24.9, thừa cân ≥25).
- Nếu hỏi về bài tập: Gợi ý bài tập phù hợp dựa trên BMI nếu có thông tin, hoặc hỏi thêm thông tin.
- Nếu hỏi về lịch tập: Hướng dẫn cách đặt lịch trong ứng dụng.
- Nếu hỏi về dinh dưỡng: Đưa ra lời khuyên chung về ăn uống lành mạnh.
- Nếu câu hỏi không liên quan đến fitness: Lịch sự chuyển hướng về chủ đề fitness hoặc trả lời ngắn gọn.
- Giữ câu trả lời ngắn gọn, dưới 200 từ.

Thông tin người dùng (nếu có): ${context || 'Không có thông tin cụ thể'}
    `;

    const response = await openai.chat.completions.create({
      model: 'gpt-3.5-turbo',
      messages: [
        { role: 'system', content: systemPrompt },
        { role: 'user', content: message }
      ],
      max_tokens: 200,
      temperature: 0.7,
    });

    const aiResponse = response.choices[0].message.content.trim();
    console.log('AI Response:', aiResponse);

    res.json({ response: aiResponse });
  } catch (error) {
    console.error('Error with OpenAI:', error);
    // Fallback response on error
    if (error.status === 429) {
      // Quota exceeded, use static responses
      const staticResponses = {
        'bmi': 'BMI (Body Mass Index) là chỉ số đo lường cân nặng tương đối với chiều cao. Công thức tính: BMI = cân nặng (kg) / (chiều cao (m))^2. Các mức độ: Thiếu cân <18.5, Bình thường 18.5-24.9, Thừa cân ≥25.',
        'bài tập': 'Dựa trên thông tin của bạn, tôi gợi ý tập cardio nhẹ nhàng như đi bộ 30 phút mỗi ngày để cải thiện sức khỏe.',
        'lịch tập': 'Bạn có thể đặt lịch tập trong trang Profile của ứng dụng. Chọn ngày, tiêu đề, mục tiêu và thời gian tập luyện.',
        'dinh_duong': 'Ăn uống lành mạnh bao gồm rau xanh, protein nạc, tinh bột phức tạp và hạn chế đường. Uống đủ nước và ăn cân bằng.',
        'default': 'Tôi là chatbot trợ lý fitness. Tôi có thể giúp bạn về BMI, bài tập, lịch tập và dinh dưỡng. Bạn cần hỗ trợ gì?'
      };
      const lowerMessage = (req.body.message || '').toLowerCase();
      let response = staticResponses.default;
      if (lowerMessage.includes('bmi')) response = staticResponses.bmi;
      else if (lowerMessage.includes('bài tập') || lowerMessage.includes('tập luyện')) response = staticResponses['bài tập'];
      else if (lowerMessage.includes('lịch tập') || lowerMessage.includes('lịch')) response = staticResponses['lịch tập'];
      else if (lowerMessage.includes('dinh dưỡng') || lowerMessage.includes('ăn uống')) response = staticResponses.dinh_duong;
      res.json({ response });
    } else {
      res.json({ response: 'Xin lỗi, có lỗi xảy ra. Bạn có thể hỏi về BMI, bài tập, lịch tập hoặc dinh dưỡng để được hỗ trợ.' });
    }
  }
};

module.exports = { chatWithAI };
