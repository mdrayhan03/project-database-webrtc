document.addEventListener("DOMContentLoaded", function() {
    const currentPage = window.location.pathname.split('/').pop();
    
    if (currentPage === 'index.html' || currentPage === '') {
        setupIndexPage();
    } else if (currentPage === 'meeting.html') {
        setupMeetingPage();
    }
});

function setupIndexPage() {
    const buzzID = document.getElementById("buzzID");
    const joinBuzzBtn = document.getElementById("joinBuzzBtn");

    if (buzzID && joinBuzzBtn) {
        buzzID.addEventListener("input", function() {
            if (this.value.trim() !== "") {
                joinBuzzBtn.classList.remove("disabled");
                joinBuzzBtn.href = "meeting.html?room=" + encodeURIComponent(this.value.trim());
            } else {
                joinBuzzBtn.classList.add("disabled");
                joinBuzzBtn.removeAttribute("href");
            }
        });

        joinBuzzBtn.addEventListener("click", async function(event) {
            event.preventDefault();
            const meetingCode = buzzID.value.trim();

            if (await validateMeetingCode(meetingCode)) {
                const isLoggedIn = localStorage.getItem("buzzyLoggedIn") === "true";

                if (isLoggedIn) {
                    window.location.href = `meeting.html?room=${meetingCode}`;
                } else {
                    window.location.href = `guest_join.html?room=${meetingCode}`;
                }
            }
        });
    }
}

// Function to check if the entered meeting code is valid and active
async function validateMeetingCode(meetingCode) {
    const codePattern = /^[a-z]{3}-[a-z]{3}-[a-z]{3}$/;

    if (!codePattern.test(meetingCode)) {
        alert("Invalid meeting code format! Please use the format abc-abc-abc.");
        return false;
    }

    // Simulating a backend check (Replace with actual API call when backend is ready)
    /*
    try {
        const response = await fetch("/api/checkMeeting", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code: meetingCode })
        });

        const data = await response.json();

        if (!data.valid) {
            alert("Invalid or inactive meeting code. Please check and try again.");
            return false;
        }
        return true;
    } catch (error) {
        console.error("Error checking meeting code:", error);
        alert("Unable to verify meeting code. Please try again later.");
        return false;
    }
    */

    return true; // Temporary return (remove when backend is implemented)
}

function setupMeetingPage() {
    const urlParams = new URLSearchParams(window.location.search);
    const roomId = urlParams.get('room') || generateMeetingId();
    const isAdmin = urlParams.get('isAdmin') === 'true';
    const isGuest = urlParams.get('isGuest') === 'true';

    document.getElementById("meetingCodeDisplay").textContent = roomId;
    document.getElementById("localParticipantName").textContent = localStorage.getItem("buzzyUsername") || "You";

    if (!isAdmin) {
        document.getElementById("adminPanel").style.display = "none";
    }

    if (isGuest) {
        restrictGuestPermissions();
    }

    setupControlButtons();
    setupChatFunctionality();
    setupParticipantsList();
    setupAdminPanelAndMeetingCode();
    setupAdminButtons();
}

function generateMeetingId() {
    return Array(3).fill(0).map(() => Math.random().toString(36).substr(2, 3)).join('-');
}

function setupAdminPanelAndMeetingCode() {
    const chatBox = document.getElementById('chatBox');
    const toggleRightPanel = document.getElementById('toggleRightPanel');
    const copyCodeBtn = document.getElementById('copyCodeBtn');

    copyCodeBtn.addEventListener('click', function () {
        navigator.clipboard.writeText(document.getElementById('meetingCodeDisplay').textContent)
            .then(() => alert('Meeting code copied!'));
    });

    toggleRightPanel.addEventListener('click', function () {
        chatBox.classList.toggle('active');
        toggleRightPanel.querySelector('i').className = 
            chatBox.classList.contains('active') ? 'fas fa-times' : 'fas fa-comment';
    });
}

function setupControlButtons() {
    document.getElementById("toggleMic").addEventListener("click", function() {
        toggleMediaTrack("audio");
    });

    document.getElementById("toggleVideo").addEventListener("click", function() {
        toggleMediaTrack("video");
    });
}

function toggleMediaTrack(type) {
    const videoElement = document.getElementById("localVideo");
    if (videoElement.srcObject) {
        const track = videoElement.srcObject.getTracks().find(t => t.kind === type);
        if (track) {
            track.enabled = !track.enabled;
        }
    } else {
        console.warn(`No ${type} stream found`);
    }
}

function setupChatFunctionality() {
    const sendMessageBtn = document.getElementById('sendMessageBtn');
    const messageInput = document.getElementById('messageInput');
    const chatMessages = document.getElementById('chatMessages');

    sendMessageBtn.addEventListener("click", sendChatMessage);
    messageInput.addEventListener("keypress", function(event) {
        if (event.key === "Enter") sendChatMessage();
    });
}

function sendChatMessage() {
    const messageInput = document.getElementById('messageInput');
    if (messageInput.value.trim() !== "") {
        document.getElementById('chatMessages').innerHTML += `<div class='chat-message'><p>${messageInput.value}</p></div>`;
        messageInput.value = "";
    }
}

function setupParticipantsList() {
    const participantsList = document.getElementById("participantsList");
    const toggleParticipants = document.getElementById("toggleParticipants");
    const closeParticipantsList = document.getElementById("closeParticipantsList");

    toggleParticipants.addEventListener("click", function () {
        participantsList.classList.toggle('active');
    });

    closeParticipantsList.addEventListener("click", function () {
        participantsList.classList.remove('active');
    });
}

// document.getElementById("endCall").addEventListener("click", function () {
//     if (confirm("Are you sure you want to leave the meeting?")) {
//         window.location.href = "index.html"; // Redirect to homepage
//     }
// });

// Restrict guest users in the meeting room
function restrictGuestPermissions() {
    console.log("Guest mode activated - restricting permissions.");

    document.getElementById("adminPanel").style.display = "none"; // Hide admin panel
    document.getElementById("shareScreen").disabled = true; // Disable screen sharing
    document.getElementById("toggleParticipants").disabled = true; // Disable participants list
    document.getElementById("toggleRightPanel").disabled = false; // Allow chat access

    // Ensure guests can only toggle their own mic/video
    document.getElementById("toggleMic").disabled = false;
    document.getElementById("toggleVideo").disabled = false;
}
