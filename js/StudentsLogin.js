// Include all the neccessary javascripts checks For StudentLogin.html
function validateForm() {
    var studentEmail = document.getElementById("student-email").value;
    var studentPassword = document.getElementById("student-password").value;
  
    // Check if Student Email or Student Password fields are empty
    if (studentEmail === "" || studentPassword === "") {
      alert("Both Student Email and Password are required.");
      return false; // Prevent form submission
    }
  
    // Additional validation logic can be added here if needed
  
    // If all checks pass, allow form submission
    return true;
  }
  