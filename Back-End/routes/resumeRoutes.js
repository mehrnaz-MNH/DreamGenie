import { Router } from "express";
import upload from "../utils/multerConfig.js";
import uploadResume from "../controllers/resumeControllers.js";

const router = Router()


router.post('/upload', upload.single('file'), uploadResume)

export default router


