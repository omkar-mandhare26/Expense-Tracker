document.querySelector("#submitbtn").addEventListener("click", async (e) => {
    e.preventDefault();

    const name = document.querySelector("#name").value.trim();
    const price = document.querySelector("#price").value.trim();

    if (!name || isNaN(price) || price <= 0) {
        alert("Please enter a valid name and price.");
        return;
    }

    try {
        const res = await fetch(`/insertdata?name=${name}&price=${price}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            }
        });

        alert("Expense Added")
        window.location.href = '/';
    } catch (error) {
        console.error("Error:", error);
        alert("Error occurred while adding expense.");
    }
});
