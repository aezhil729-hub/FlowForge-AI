const API = "http://127.0.0.1:8000";

// BUTTON CLICK FUNCTION
async function generateWorkflow() {

    console.log("✅ Button clicked");

    const prompt = document.getElementById("prompt").value;

    const workflowBox = document.getElementById("workflow");
    const logs = document.getElementById("logs");

    logs.innerText = "🧠 Generating workflow...";

    try {
        const response = await fetch(${API}/generate-workflow, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ prompt })
        });

        const data = await response.json();

        console.log("API RESPONSE:", data);

        logs.innerText = "✅ Workflow generated successfully";

        renderFlow(data);

    } catch (error) {
        console.error(error);
        logs.innerText = "❌ Error: " + error.message;
    }
}


// RENDER WORKFLOW UI
function renderFlow(data) {

    const container = document.getElementById("workflow");

    container.innerHTML = "";

    // backend structure safe check
    let steps = data.steps || data.workflow || [
        "Form Submitted",
        "Send Email",
        "Notify Discord"
    ];

    steps.forEach((step, index) => {

        container.innerHTML += `
            <div class="node">
                ${index + 1}. ⚡ ${step}
            </div>
        `;
    });
}