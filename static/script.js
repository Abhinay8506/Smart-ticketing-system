function raiseTicket() {
    const description = document.getElementById("description").value;

    if (!description.trim()) {
        alert("Please enter a description");
        return;
    }

    fetch("/raise_ticket", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: "description=" + encodeURIComponent(description)
    })
    .then(res => res.json())
    .then(data => {
        if (data.position === 0) {
            document.getElementById("result").innerText =
                "Your ticket is currently IN PROGRESS";
        } else {
            document.getElementById("result").innerText =
                "Tickets before you: " + data.position;
        }
    });
}

function processNextTicket() {
    fetch("/process_next", {
        method: "POST"
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("admin-result").innerText =
            data.message + (data.ticket_id ? ` (Ticket ID: ${data.ticket_id})` : "");

        setTimeout(() => {
            location.reload();
        }, 1000);
    });
}

