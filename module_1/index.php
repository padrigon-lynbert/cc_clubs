<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SMS3</title>

  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css">
  <link rel="stylesheet" href="../style.css">

  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.13.1/font/bootstrap-icons.min.css">
  <style>
    @import url("../style.css");

    /* Make sidebar scrollable in landscape mode on mobile devices */
    @media (max-width: 768px) and (orientation: landscape) {
      .sidebar {
        max-height: 100vh;
        overflow-y: auto;
      }
    }
  </style>
</head>
<body>
  <!-- navbar -->
  <div class="sidebar">
    <nav class="nav flex-column">
    <a href="#" class="nav-link navbar-brand">
    <span class="icon"><i class="bi bi-grid"></i></span>
    <span class="navbar-brand description">SMS 3</span> 
    </a>
    <a href="#" class="nav-link active">
    <i class="bi bi-bar-chart"></i>

    <span class="description">Module 1</span> 
    </a>
    <a href="#" class="nav-link">
    <i class="bi bi-bar-chart"></i>

    <span class="description">Module 2</span> 
    </a>
  
    <a href="#" class="nav-link">
    <i class="bi bi-bar-chart"></i>

    <span class="description">Module 3</span> 
    </a>
    <a href="#" class="nav-link">
    <i class="bi bi-bar-chart"></i>

    <span class="description">Module 4</span> 
    </a>
    <a href="#" class="nav-link">
    <i class="bi bi-bar-chart"></i>

    <span class="description">Module 5</span> 
    </a>
    <a href="#" class="nav-link">
    <i class="bi bi-bar-chart"></i>

    <span class="description">Module 6</span> 
    </a>
    <a href="#" class="nav-link">
    <i class="bi bi-bar-chart"></i>

    <span class="description">Module 7</span> 
    </a>
    <a href="#" class="nav-link">
    <i class="bi bi-bar-chart"></i>

    <span class="description">Module 8</span> 
    </a>
    <a href="#" class="nav-link">
    <i class="bi bi-bar-chart"></i>

    <span class="description">Module 9</span> 
    </a>
    <a href="#" class="nav-link">
    <i class="bi bi-bar-chart"></i>

    <span class="description">Module 10</span> 
    </a>

    
  </nav>
  </div>

  <div class="main-content flex-grow-1">

  <div class=" " >
    <ul class="nav nav-tabs" id="myTab" role="tablist">
      <li class="nav-item" role="presentation">
        <button class="nav-link active" id="submodule1-tab" data-bs-toggle="tab" data-bs-target="#submodule1" type="button" role="tab" aria-controls="submodule1" aria-selected="true">Sub-Module 1</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" id="submodule2-tab" data-bs-toggle="tab" data-bs-target="#submodule2" type="button" role="tab" aria-controls="submodule2" aria-selected="false">Sub-Module 2</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" id="submodule3-tab" data-bs-toggle="tab" data-bs-target="#submodule3" type="button" role="tab" aria-controls="submodule3" aria-selected="false">Sub-Module 3</button>
      </li>
      <li class="nav-item" role="presentation">
        <button class="nav-link" id="submodule4-tab" data-bs-toggle="tab" data-bs-target="#submodule4" type="button" role="tab" aria-controls="submodule4" aria-selected="false">Sub-Module 4</button>
      </li>
    </ul>


    <div class="tab-content " id="myTabContent">

      <!-- submodule 1 -->
      <div class="tab-pane fade show active" id="submodule1" role="tabpanel" aria-labelledby="submodule1-tab">
        <p>Content for Sub-Module 1</p>
      </div>
      <!-- submodule 2 -->
      <div class="tab-pane fade" id="submodule2" role="tabpanel" aria-labelledby="submodule2-tab">
        <p>Content for Sub-Module 2</p>
      </div>
      <!-- submodule 3 -->
      <div class="tab-pane fade" id="submodule3" role="tabpanel" aria-labelledby="submodule3-tab">
        <p>Content for Sub-Module 3</p>
      </div>
      <!-- submodule 4 -->
      <div class="tab-pane fade" id="submodule4" role="tabpanel" aria-labelledby="submodule4-tab">
        <p>Content for Sub-Module 4</p>
      </div>
    </div>


    
  </div>

  </div>

  <footer class="mt-auto bg-light">
    <div class="container text-center">
      <p class="text-muted">© 2023 Your Company. All rights reserved.</p>
    </div>
  </footer>

  
  </style>
</body>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
</html>