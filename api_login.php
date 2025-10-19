<?php
header('Content-Type: application/json');

$host = "dpg-d3q794odl3ps73bn4jbg-a.oregon-postgres.render.com";
$db   = "reporting_api";
$user = "reporting_api_user";
$pass = "NnJaaGQZdlomaoT22c5bXfZHqytGrfB2";
$port = "5432";

try {
    $dsn = "pgsql:host=$host;port=$port;dbname=$db;";
    $conn = new PDO($dsn, $user, $pass, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION
    ]);
} catch (PDOException $e) {
    echo json_encode(["status" => "error", "message" => "DB connection failed"]);
    exit;
}

$data = json_decode(file_get_contents("php://input"), true);
$acc_no = $data["acc_no"] ?? "";
$pass   = $data["password"] ?? "";

$sql = "SELECT id, acc_no, name, role FROM users WHERE acc_no = :acc_no AND password = :password";
$stmt = $conn->prepare($sql);
$stmt->execute([
    ":acc_no"   => $acc_no,
    ":password" => $pass
]);

$user = $stmt->fetch(PDO::FETCH_ASSOC);

if ($user) {
    echo json_encode(["status" => "success", "user" => $user]);
} else {
    echo json_encode(["status" => "fail", "message" => "Invalid login"]);
}
