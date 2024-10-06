document.querySelector("#delete").addEventListener("click", async (e) => {
    e.preventDefault();
    try {
        const res = await fetch("/deleteallDB", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            }
        });
        alert("Expenses Deleted")
        location.reload();
    } catch (error) {
        console.error("Error:", error);
        alert("Error occurred while deleting records.");
    }
});
