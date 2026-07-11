const API = "https://hive-os-backend.onrender.com";

export async function sendMessage(message) {
  const res = await fetch(`${API}/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      message,
    }),
  });

  if (!res.ok) {
    throw new Error("Backend Error");
  }

  return await res.json();
}