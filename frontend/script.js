document.getElementById("generate").addEventListener("click", function () {
    let text = document.getElementById("text").value.trim();

    if (text === "") {
        alert("Please enter some text.");
        return;
    }

    alert("🎉 Indian TTS AI is coming soon!\n\nYou entered:\n" + text);
});document.querySelector("button").addEventListener("click", () => {
  alert("Indian TTS is under development.");
});
