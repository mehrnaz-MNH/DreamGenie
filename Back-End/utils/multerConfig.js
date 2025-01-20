import multer from "multer";
import path from "path";

const storage = multer.diskStorage({
    destination: (req, file, cb) => {

        cb(null, 'uploads/')

    },
    filename: (req, file, cb) => {

        const ext = path.extname(file.originalname);
        cb(null, `${Date.now()}-${file.filename}-${ext}`);

    }
})

const fileFilter = (req, file, cb) => {
    const ext = path.extname(file.originalname);
    if (ext === '.pdf' || ext === '.docx') {
        cb(null, true)
    } else {
        cb(new Error('only pdf and word docs are allowed!'), false)
    }
}

const upload = multer({
    storage,
    fileFilter
})

export default upload
