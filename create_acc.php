<?php
// create_acc.php using PDO

$host = "dpg-d35pt5ali9vc738k5ur0-a.oregon-postgres.render.com";
$db   = "temp_api";
$user = "temp_api_user";
$pass = "cTWduHqplZ2sAc00VaGblaNnZcFTqkmj";
$port = "5432";

$message = "";

try {
    $conn = new PDO("pgsql:host=$host;port=$port;dbname=$db", $user, $pass);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Connection failed: " . $e->getMessage());
}

// Handle account creation
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $role = $_POST['role'];

    $role_names = [
        0 => 'student',
        1 => 'officer',
        2 => 'adviser',
        3 => 'activitycoordinator',
        4 => 'admin'
    ];

    $name = $role_names[$role];
    $password = $name; // password same as name

    try {
        // Get next id from sequence
        $stmt = $conn->query("SELECT nextval('users_id_seq') AS next_id");
        $next_id = $stmt->fetch(PDO::FETCH_ASSOC)['next_id'];
        $acc_no = str_pad($next_id, 4, "0", STR_PAD_LEFT);

        // Insert user
        $insert = $conn->prepare("INSERT INTO users (id, acc_no, name, password, role) VALUES (?, ?, ?, ?, ?)");
        $insert->execute([$next_id, $acc_no, $name, $password, $role]);

        // Redirect to prevent double submission
        header("Location: " . $_SERVER['PHP_SELF'] . "?success=1&acc_no=$acc_no&name=$name&password=$password");
        exit();
    } catch (PDOException $e) {
        $message = "Error creating account: " . $e->getMessage();
    }
}

// Check success message
if (isset($_GET['success']) && $_GET['success'] == 1) {
    $acc_no = htmlspecialchars($_GET['acc_no']);
    $name = htmlspecialchars($_GET['name']);
    $password = htmlspecialchars($_GET['password']);
    $message = "Account created successfully!<br>Acc No: $acc_no<br>Name: $name<br>Password: $password";
}

// Fetch users for table
$stmt = $conn->query("SELECT acc_no, name FROM users ORDER BY id ASC");
$users = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>

<!DOCTYPE html>
<html>
<head>
    <title>Create Account</title>
</head>
<body>
<h2>Create New Account</h2>

<form method="post">
    <label for="role">Select Role:</label>
    <select name="role" id="role">
        <option value="0">Student</option>
        <option value="1">Officer</option>
        <option value="2">Adviser</option>
        <option value="3">Activity Coordinator</option>
        <option value="4">Admin</option>
    </select>
    <button type="submit">Create Account</button>
</form>

<h2>Users List</h2>
<div style="max-height: 500px; overflow-y: auto; border: 1px solid #ccc;">
    <table border="1" width="100%" cellspacing="0" cellpadding="5">
        <thead>
            <tr>
                <th>Acc ID</th>
                <th>Name</th>
            </tr>
        </thead>
        <tbody>
            <?php
            if ($users) {
                foreach ($users as $row) {
                    echo "<tr>";
                    echo "<td>" . htmlspecialchars($row['acc_no']) . "</td>";
                    echo "<td>" . htmlspecialchars($row['name']) . "</td>";
                    echo "</tr>";
                }
            } else {
                echo "<tr><td colspan='2'>No users found.</td></tr>";
            }
            ?>
        </tbody>
    </table>
</div>

<div>
    <?php if ($message) echo $message; ?>
</div>

<?php
$conn = null; // close connection
?>
</body>
</html>