const API = "http://127.0.0.1:8000";

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