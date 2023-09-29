// Include all the neccessary Java Script Here For EmployeeLogin.html page
function validateForm() {
  var employeeId = document.getElementById("employee-id").value;
  var employeePassword = document.getElementById("employee-password").value;

  // Check if the Employee ID field is empty
  if (employeeId === "") {
    alert("Please enter your Employee ID");
    return false; // Prevent form submission
  }

  // Check if the Employee Password field is empty
  if (employeePassword === "") {
    alert("Please enter your Password");
    return false; // Prevent form submission
  }

  // If all checks pass, allow form submission
  return true;
}