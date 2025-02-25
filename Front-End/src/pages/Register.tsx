import React, { FormEvent, useState } from "react";

const Register = () => {
  const [username, setUserName] = useState<string>("");
  const [email, setEmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [err, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);

  async function handleSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setError(null);
    setSuccess(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user_name: username,
          email: email,
          password: password,
        }),
      });
      console.log(response);

      if (!response.ok) {
        console.log("here");
        const data = await response.json();
        console.log(data);
        // If the response is not ok, show the error
        setError(data.detail ? data.detail : "Something went wrong");
        console.log(err);
        return;
      }

      // If registration is successful, show the success message
      setSuccess("Registration successful! You can now log in.");
      // eslint-disable-next-line @typescript-eslint/no-unused-vars
    } catch (error) {
      // Handle unexpected errors, such as network issues
      setError("An unexpected error occurred. Please try again later.");
    }
  }

  return (
    <div className="flex justify-center items-center min-h-screen bg-white text-black">
      <div className="w-96 bg-white p-6 rounded-lg shadow-lg border border-gray-300">
        <h2 className="text-3xl font-bold text-center mb-6">Register</h2>

        {/* Error and Success Messages */}
        {err && (
          <div className="flex items-center gap-2 bg-gray-100 text-black p-3 rounded-lg mb-4 border border-black">
            ⚠️ {err}
          </div>
        )}
        {success && (
          <div className="flex items-center gap-2 bg-gray-100 text-black p-3 rounded-lg mb-4 border border-black">
            ✅ {success}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4">
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUserName(e.target.value)}
            className="w-full p-2 bg-white border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-black"
          />
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="w-full p-2 bg-white border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-black"
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full p-2 bg-white border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-black"
          />
          <button
            type="submit"
            className="w-full bg-black text-white p-2 rounded-md hover:bg-gray-900 transition"
          >
            Register
          </button>
        </form>
      </div>
    </div>
  );
};

export default Register;
