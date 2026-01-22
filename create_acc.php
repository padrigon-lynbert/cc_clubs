<?php
$host = "dpg-d5hpka6r433s73btsgh0-a.oregon-postgres.render.com";
$db   = "temp_api_u2s1";
$user = "admin";
$pass = "LGQ9jgQyhjmYP0OfQQITZJP1CTzxzP2q";
$port = "5432";

try {
    $conn = new PDO(
        "pgsql:host=$host;port=$port;dbname=$db",
        $user,
        $pass,
        [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]
    );
} catch (PDOException $e) {
    die("DB connection failed");
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $role  = (int)$_POST['role'];
    $email = $_POST['email'];

    $role_names = [
        0 => 'student',
        1 => 'officer',
        2 => 'adviser',
        3 => 'activitycoordinator',
        4 => 'admin'
    ];

    if (!isset($role_names[$role])) {
        die("Invalid role");
    }

    $name = $role_names[$role];
    $password = $name;

    $stmt = $conn->prepare(
        "INSERT INTO users (email, name, password, role)
         VALUES (:email, :name, :password, :role)"
    );

    $stmt->execute([
        ':email'    => $email,
        ':name'     => $name,
        ':password' => $password,
        ':role'     => $role
    ]);

    echo "Account created";
    exit;
}
?>
