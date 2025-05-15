const fetch = require("node-fetch");

exports.handler = async function(event) {
  if (event.httpMethod !== "POST") {
    return { statusCode: 405, body: "Method Not Allowed" };
  }

  try {
    const { text, targetLang, sourceLang } = JSON.parse(event.body);

    const response = await fetch("https://libretranslate.de/translate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        q: text,
        source: sourceLang || "auto",
        target: targetLang,
        format: "text"
      }),
    });

    const data = await response.json();

    return {
      statusCode: 200,
      body: JSON.stringify({ translatedText: data.translatedText }),
    };
  } catch (error) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: error.message }),
    };
  }
};
