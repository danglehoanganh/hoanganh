const express = require("express");
const { getProfile, getSchedules, updateSchedules, updateProfile, getExerciseResults, updateExerciseResults } = require("../controllers/profileController");
const router = express.Router();

router.get("/profile", getProfile);
router.get("/schedules", getSchedules);
router.put("/schedules", updateSchedules);
router.put("/profile", updateProfile);
router.get("/exerciseResults", getExerciseResults);
router.put("/exerciseResults", updateExerciseResults);

module.exports = router;
