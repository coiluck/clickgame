let counterDisplay = document.getElementById("counter");

// 初期値取得
fetch("/get_count")
    .then(res => res.json())
    .then(data => {
        counterDisplay.textContent = data.count;
    });

// bodyクリックでカウント増加
document.body.addEventListener("click", () => {
    console.log("クリック検出")
    fetch("/click", {
        method: "POST"
    })
    .then(res => res.json())
    .then(data => {
        counterDisplay.textContent = data.count;
    });
    console.log("クリックshorikannryou")
});

document.addEventListener('DOMContentLoaded', () => {
    console.log("読み込み完了");
});