<?php
header('Content-Type: application/json');

$host = "153.92.15.81";
$db   = "u514031374_sisreg";
$user = "u514031374_sisreg";
$pass = "sisregP@55w0rd";

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

if (!$email || !$password) {
    echo json_encode(["status"=>"fail","message"=>"Email and password required"]);
    exit;
}

// join with personalinfo to get CurrentCourse
$stmt = $pdo->prepare("
    SELECT u.id, u.name, u.email, u.role, u.password,
           p.CurrentCourse
    FROM users u
    LEFT JOIN personalinfo p ON u.PersonalID = p.PersonalID
    WHERE u.email = :email
    LIMIT 1
");
$stmt->execute([":email" => $email]);
$user = $stmt->fetch(PDO::FETCH_ASSOC);

if ($user && $password === $user['password']) {

    // split full name
    $parts = explode(" ", $user['name']);
    $first_name = $parts[0] ?? "";
    $last_name  = $parts[count($parts)-1] ?? "";
    $middle_name = count($parts) > 2 ? implode(" ", array_slice($parts,1,count($parts)-2)) : "";

    echo json_encode([
        "status" => "success",
        "user" => [
            "id"          => $user['id'],
            "first_name"  => $first_name,
            "middle_name" => $middle_name,
            "last_name"   => $last_name,
            "email"       => $user['email'],
            "role"        => $user['role'],
            "department"  => $user['CurrentCourse'] ?? null
        ]
    ]);
} else {
    echo json_encode(["status"=>"fail","message"=>"Invalid login"]);
}
