<?php
header('Content-Type: application/json');

$host = "153.92.15.81";
$db   = "u514031374_fms3";
$user = "u514031374_fms3";
$pass = "fms3P@55w0rd";

try {
    $pdo = new PDO(
        "mysql:host=$host;dbname=$db;charset=utf8mb4",
        $user,
        $pass,
        [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]
    );
} catch (PDOException $e) {
    echo json_encode(["status"=>"error","message"=>"DB connection failed"]);
    exit;
}

$data = json_decode(file_get_contents("php://input"), true);
$email = $data['email'] ?? '';
$password = $data['password'] ?? '';

$stmt = $pdo->prepare("
    SELECT id, first_name, middle_name, last_name, email, role, department, password
    FROM faculties
    WHERE email = :email
    LIMIT 1
");
$stmt->execute([":email" => $email]);
$user = $stmt->fetch(PDO::FETCH_ASSOC);

if ($user && password_verify($password, $user['password'])) {
    echo json_encode([
        "status" => "success",
        "user" => [
            "id" => $user['id'],    
            "first_name" => $user['first_name'],
            "middle_name" => $user['middle_name'],
            "last_name" => $user['last_name'],
            "email" => $user['email'],
            "role" => $user['role'],
            "department" => $user['department']
        ]
    ]);
} else {
    echo json_encode(["status"=>"fail","message"=>"Invalid login"]);
}
