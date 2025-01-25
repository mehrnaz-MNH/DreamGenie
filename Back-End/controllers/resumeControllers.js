const uploadResume = ((req, res) => {
    try {

        if (!req.file) {

            return res.status(400).json({ message: 'No file uploaded' })
        }


        console.log(req.file)

        return res.status(200).json({
            message: "file uploaded !",
            file: req.file
        })


    } catch (error) {

        return res.status(500).json({ message: 'something went wrong while uploading , please try again !' })

    }

})

export default uploadResume


