import express from "express";
import resumeRoutes from './routes/resumeRoutes.js'


const app = express();

app.use(express.json());

app.use(express.urlencoded({ extended: true }))


app.use('/api/resume', resumeRoutes)

export default app;
