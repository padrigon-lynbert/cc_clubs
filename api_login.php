<?php
header('Content-Type: application/json');

$host = "dpg-d5hpka6r433s73btsgh0-a.oregon-postgres.render.com";
$db   = "temp_api_u2s1";
$user = "admin";
$pass = "LGQ9jgQyhjmYP0OfQQITZJP1CTzxzP2q";
$port = "5432";

try {
    $dsn = "pgsql:host=$host;port=$port;dbname=$db";
    $conn = new PDO($dsn, $user, $pass, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION
    ]);
} catch (PDOException $e) {
    echo json_encode([
        "status" => "error",
        "message" => "DB connection failed"
    ]);
    exit;
}

$data = json_decode(file_get_contents("php://input"), true);

$email    = $data["email"] ?? "";
$password = $data["password"] ?? "";

$sql = "
    SELECT id, email, name, role
    FROM users
    WHERE email = :email
      AND password = :password
";

$stmt = $conn->prepare($sql);
$stmt->execute([
    ":email"    => $email,
    ":password" => $password
]);

$user = $stmt->fetch(PDO::FETCH_ASSOC);

if ($user) {
    echo json_encode([
        "status" => "success",
        "user"   => $user
    ]);
} else {
    echo json_encode([
        "status"  => "fail",
        "message" => "Invalid login"
    ]);
}
