<?php
// create_account (render)

$host = "dpg-d35pt5ali9vc738k5ur0-a.oregon-postgres.render.com";
$db   = "temp_api";
$user = "temp_api_user";
$pass = "cTWduHqplZ2sAc00VaGblaNnZcFTqkmj";
$port = "5432";

$conn = pg_connect("host=$host port=$port dbname=$db user=$user password=$pass");

if (!$conn) {
    die("Connection failed: " . pg_last_error());
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

    // Get next id from sequence
    $id_result = pg_query($conn, "SELECT nextval('users_id_seq') AS next_id");
    if ($id_result) {
        $row = pg_fetch_assoc($id_result);
        $next_id = $row['next_id'];
        $acc_no = str_pad($next_id, 4, "0", STR_PAD_LEFT);

        $query = "INSERT INTO users (id, acc_no, name, password, role) VALUES ($1, $2, $3, $4, $5)";
        $result_insert = pg_query_params($conn, $query, [$next_id, $acc_no, $name, $password, $role]);

        if ($result_insert) {
            // Redirect to avoid duplicate insert on refresh
            header("Location: " . $_SERVER['PHP_SELF'] . "?success=1&acc_no=$acc_no&name=$name&password=$password");
            exit();
        } else {
            $message = "Error creating account: " . pg_last_error();
        }
    } else {
        $message = "Error fetching next ID: " . pg_last_error();
    }
}

// Check if redirected after success
$message = "";
if (isset($_GET['success']) && $_GET['success'] == 1) {
    $acc_no = htmlspecialchars($_GET['acc_no']);
    $name = htmlspecialchars($_GET['name']);
    $password = htmlspecialchars($_GET['password']);
    $message = "Account created successfully!<br>Acc No: $acc_no<br>Name: $name<br>Password: $password";
}

// Fetch users for table
$query_users = "SELECT acc_no, name FROM users ORDER BY id ASC";
$result_users = pg_query($conn, $query_users);

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
            if ($result_users && pg_num_rows($result_users) > 0) {
                while ($row = pg_fetch_assoc($result_users)) {
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
// Close connection once at the end
pg_close($conn);
?>
</body>
</html>
