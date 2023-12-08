function loadCustomNavbar(){
    var customNavBar =  `
    <section style="height: 0vh;" id="nav">
    <header>
            <nav class="navbar bg-body-tertiary">
                <div class="container-fluid">
                    <a class="navbar-brand" href="#">
                    <img src="assets/img/logo2.png" alt="Logo" width="50" height="50" class="d-inline-block align-text-top">
                        ASISTENCIA QR
                    </a>

                    <div class="letra ms-auto">       
                        <a href="descargar.html">DescargarAPP</a>
                    </div>
                </div>
            </nav>
    </header>
<section ><br>



    `;

    var customNabBarHTML = document.getElementById("custom-navbar");
    customNabBarHTML.innerHTML = customNavBar;
}

loadCustomNavbar();