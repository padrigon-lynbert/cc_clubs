<?php
// connect to MySQL
$conn = new mysqli("localhost", "root", "", "test_login");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// process login
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $acc_no = $_POST["acc_no"];
    $pass   = $_POST["password"];

    // query db
    $sql = "SELECT * FROM users WHERE acc_no='$acc_no' AND password='$pass'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        echo " Welcome, " . $row["name"] . " (Role: " . $row["role"] . ")";
    } else {
        echo " Invalid login.";
    }
}
?>

<form method="post">
    <input type="text" name="acc_no" placeholder="Account No" required>
    <input type="password" name="password" placeholder="Password" required>
    <button type="submit">Login</button>
</form>
