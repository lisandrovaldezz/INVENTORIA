// Selección de elementos
const loginButton = document.getElementById("login-button");
const registerButton = document.getElementById("register-button");
const loginModal = document.getElementById("login-modal");
const registerModal = document.getElementById("register-modal");
const closeButtons = document.querySelectorAll(".close");
const userIcon = document.getElementById("user-icon");
const milistaButton = document.getElementById("milista-button");
const registerErrorDiv = document.getElementById('register-error');
const loginErrorDiv = document.getElementById('login-error');
const passwordInput = document.getElementById('registerForm');
const passwordHint = document.getElementById('password-hint');


// Función para abrir un modal
function openModal(modal) {
    modal.style.display = "flex";
}

// Función para cerrar un modal
function closeModal(modal) {
    modal.style.display = "none";
}

// Abrir modales
loginButton.addEventListener("click", () => openModal(loginModal));
registerButton.addEventListener("click", () => openModal(registerModal));

// Cerrar modales al hacer clic en la "x"
closeButtons.forEach((button) => {
    button.addEventListener("click", () => {
        const modal = button.closest(".modal");
        closeModal(modal);
        resetForm(modal);
    });
});

// Cerrar modal al hacer clic fuera del contenido
window.addEventListener("click", (event) => {
    if (event.target.classList.contains("modal")) {
        closeModal(event.target);
        resetForm(event.target);
    }
});

function resetForm(modal) {
    const form = modal.querySelector("form");
    if (form) form.reset();
}

// Capturar los formularios
const loginForm = document.querySelector("#login-modal form");
const registerForm = document.querySelector("#register-modal form");


document.getElementById('registerForm').addEventListener('submit', async function(event) {
  event.preventDefault();
  registerErrorDiv.textContent = '';

  const formData = new FormData(this);
  const data = {
    email: formData.get('email'),
    username: formData.get('username'),
    password: formData.get('password')
  };
  const response = await fetch('http://127.0.0.1:8000/register/', {

    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });

  const result = await response.json();
  if (response.ok) {
  closeModal(registerModal);
  alert("Registro exitoso");
} else {
  // Mostrar mensaje de error:
  if (result.detail) {
    if (typeof result.detail === 'string') {
      registerErrorDiv.textContent = result.detail;
    } else if (Array.isArray(result.detail)) {
      registerErrorDiv.textContent = result.detail.map(e => e.msg).join(', ');
    } else {
      registerErrorDiv.textContent = "Error en el registro.";
    }

    registerErrorDiv.style.display = 'block'; // mostrar mensaje
    registerErrorDiv.classList.remove('fade-out'); // por si quedó de antes

    setTimeout(() => {
      registerErrorDiv.classList.add('fade-out');
      setTimeout(() => {
        registerErrorDiv.style.display = 'none';
        registerErrorDiv.classList.remove('fade-out');
      }, 500); // tiempo del fade
    }, 1500); // tiempo visible antes del fade
  }
}
});


document.getElementById('loginForm').addEventListener('submit', async function(event) {
  event.preventDefault();

  const formData = new FormData(this);
  const data = {
    username: formData.get('username'),
    password: formData.get('password')
  };

  const response = await fetch('http://127.0.0.1:8000/login/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });

  const result = await response.json();
  console.log(result);

  if (response.ok) {
    localStorage.setItem('token', result.access_token);
    closeModal(loginModal);
    alert("Login exitoso");
    mostrarIconoUsuario();
  } else {
  if (result.detail) {
    if (typeof result.detail === 'string') {
      loginErrorDiv.textContent = result.detail;
    } else if (Array.isArray(result.detail)) {
      loginErrorDiv.textContent = result.detail.map(e => e.msg).join(', ');
    } else {
      loginErrorDiv.textContent = "Error en el login.";
    }

    loginErrorDiv.style.display = 'block';
    loginErrorDiv.classList.remove('fade-out');

    setTimeout(() => {
      loginErrorDiv.classList.add('fade-out');
      setTimeout(() => {
        loginErrorDiv.style.display = 'none';
        loginErrorDiv.classList.remove('fade-out');
      }, 500);
    }, 1500);
  }
}
});

passwordInput.password.addEventListener('focus', () => {
  passwordHint.style.display = 'block';
});

passwordInput.password.addEventListener('blur', () => {
  passwordHint.style.display = 'none';
});

function mostrarIconoUsuario() {
  document.getElementById('register-button').style.display = 'none';
  document.getElementById('login-button').style.display = 'none';
  document.getElementById('user-icon').style.display = 'inline-block';
}

window.addEventListener('load', () => {
  setTimeout(() => {
    document.getElementById('botones').classList.add('visible');
  }, 200); // 1 segundo de espera
});

const userMenu = document.getElementById('user-menu');
userMenu.style.display = 'none';

userIcon.addEventListener('click', () => {
  userMenu.style.display = userMenu.style.display === 'none' ? 'block' : 'none';
});

// Cerrar el menú si hacés clic fuera de él
window.addEventListener('click', (e) => {
  if (!userIcon.contains(e.target) && !userMenu.contains(e.target)) {
    userMenu.style.display = 'none';
  }
});

document.getElementById('logout-btn').addEventListener('click', () => {
  localStorage.removeItem('token');
  location.reload();
});


// home.html

document.addEventListener("DOMContentLoaded", function () {
  const path = window.location.pathname;

  if (path.endsWith("/home.html")) {

let indice = 0;
let total = 0;
let intervalo = null;
const itemsPorVista = 6;

function cargarCarrusel() {
  fetch("http://localhost:8000/animes")
    .then(res => res.json())
    .then(animes => {
      const container = document.getElementById("carrusel-container");
      container.innerHTML = "";

      animes.forEach(anime => {
        const item = document.createElement("div");
        item.className = "carrusel-item";
        item.innerHTML = `
          <img src="${anime.imagen}" alt="${anime.nombre}" draggable="false">
          <h3>${anime.nombre}</h3>
        `;
        container.appendChild(item);
      });

      semitotal= animes.length % itemsPorVista;
      total = animes.length - semitotal;

      iniciarIntervalo();
      actualizarCarrusel();
    })
    .catch(error => console.error("Error al cargar los animes:", error));
}

function siguiente() {
  indice++;
  actualizarCarrusel();
  reiniciarIntervalo();
}

function anterior() {
  indice--;
  actualizarCarrusel();
  reiniciarIntervalo();
}

const botonDerecha = document.getElementById("boton-derecha");
const botonIzquierda = document.getElementById("boton-izquierda");

botonDerecha.addEventListener("click", () => {
  indice++;
  actualizarCarrusel();
  reiniciarIntervalo();
});


botonIzquierda.addEventListener("click", () => {
  indice--;
  actualizarCarrusel();
  reiniciarIntervalo();
});

function actualizarCarrusel() {
  const maxIndex = Math.max(0, Math.ceil(total / itemsPorVista) - 1);

  if (indice > maxIndex) indice = 0;
  if (indice < 0) indice = maxIndex;

  const shiftPercentage = indice * 100;
  document.getElementById("carrusel-container").style.transform =
    `translateX(-${shiftPercentage}%)`;
}

function iniciarIntervalo() {
  if (intervalo) clearInterval(intervalo);
  intervalo = setInterval(() => {
    indice++;
    actualizarCarrusel();
  }, 3000);
}

function reiniciarIntervalo() {
  clearInterval(intervalo);
  iniciarIntervalo();
}


cargarCarrusel();

  }
});





// listado.html


document.addEventListener("DOMContentLoaded", function () {
  const path = window.location.pathname;

  if (path.endsWith("/listado.html")) {

function cargarListado() {
  fetch("http://localhost:8000/animes")
    .then(res => res.json())
    .then(animes => {
      const container = document.getElementById("listado-animes-container");
      container.innerHTML = "";
      animes.forEach(anime => {
        const item = document.createElement("div");
        item.className = "listado-animes-item";
        item.innerHTML = `
          <img src="${anime.imagen}" alt="${anime.nombre}" draggable="false">
          <h3>${anime.nombre}</h3>
        `;
        container.appendChild(item);
      });
    })
    .catch(error => console.error("Error al cargar los animes:", error));
}


cargarListado();



const filtroCategoriaOpciones = document.getElementById('filtro-categoria-opciones');
const botonFiltroCategoria = document.getElementById("filtro-categoria-default");
filtroCategoriaOpciones.style.display = 'none';


botonFiltroCategoria.addEventListener('click', () => {
  filtroCategoriaOpciones.style.display = filtroCategoriaOpciones.style.display === 'none' ? 'block' : 'none';
});

window.addEventListener('click', (e) => {
  if (!botonFiltroCategoria.contains(e.target) && !filtroCategoriaOpciones.contains(e.target)) {
    filtroCategoriaOpciones.style.display = 'none';
  }
});


function cargarCategoriaFiltro() {
  fetch("http://localhost:8000/Ver_categorias")
    .then(res => res.json())
    .then(categorias => {
      const container = document.getElementById("filtro-categoria-opciones-container");
      container.innerHTML = "";
      categorias.forEach(categoria => {
        const item = document.createElement("div");
        item.className = "filtro-categoria-opciones-item";
        item.innerHTML = `
          <label style="display: flex; align-items: center; gap: 5px;">
            <input type="checkbox" name="categoria" value="${categoria.nombreCategoria}">
            ${categoria.nombreCategoria}
          </label>
        `;
        container.appendChild(item);
      });
      limitarCheckboxes();
    })
    .catch(error => console.error("Error al cargar las categorias:", error));
}


cargarCategoriaFiltro();


function actualizarTextoFiltroCategoria() {
  const checkboxes = document.querySelectorAll('input[name="categoria"]:checked');
  const cantidadSeleccionadas = checkboxes.length;

  if (cantidadSeleccionadas === 0) {
    botonFiltroCategoria.childNodes[0].textContent = 'Todas';
  } else if (cantidadSeleccionadas === 1) {
    botonFiltroCategoria.childNodes[0].textContent = checkboxes[0].value;
  } else {
    botonFiltroCategoria.childNodes[0].textContent = `${cantidadSeleccionadas} seleccionadas`;
  }
}

function limitarCheckboxes() {
  const checkboxes = document.querySelectorAll('input[name="categoria"]');
  checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', () => {
      const seleccionados = document.querySelectorAll('input[name="categoria"]:checked');
      if (seleccionados.length > 4) {
        checkbox.checked = false; // Evita pasarse del límite
        return;
      }
      actualizarTextoFiltroCategoria();
    });
  });
}

const filtroOrdenar = document.getElementById('ordenar-opciones');
const botonOrdenarDefault = document.getElementById("ordenar-default");
filtroOrdenar.style.display = 'none';

botonOrdenarDefault.addEventListener('click', () => {
  filtroOrdenar.style.display = filtroOrdenar.style.display === 'none' ? 'block' : 'none';
});

window.addEventListener('click', (e) => {
  if (!botonOrdenarDefault.contains(e.target) && !filtroOrdenar.contains(e.target)) {
    filtroOrdenar.style.display = 'none';
  }
});

const opcionesOrden = document.querySelectorAll(".ordenar-opciones-item");

opcionesOrden.forEach(opcion => {
  opcion.addEventListener("click", () => {
    // Obtener el valor del input dentro del label
    const valorSeleccionado = opcion.querySelector("input").value;

    // Cambiar el texto mostrado en el div principal
    botonOrdenarDefault.childNodes[0].textContent = valorSeleccionado;

    // Ocultar el menú de opciones
    filtroOrdenar.style.display = 'none';
  });
});


  }
});




// perfil.html


document.addEventListener("DOMContentLoaded", function () {
  const path = window.location.pathname;

  if (path.endsWith("/perfil.html")) {


function decodificarJWT(token) {
  const payloadBase64 = token.split('.')[1];
  const payloadJson = atob(payloadBase64);
  return JSON.parse(payloadJson);
}

async function cargarDatosUsuario() {
  const token = localStorage.getItem("token");
  if (!token) return;

  const payload = decodificarJWT(token);
  const username = payload.sub;

  try {
    const res = await fetch(`http://localhost:8000/usuario/${username}`, {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    const usuario = await res.json();

    document.getElementById("nombre-usuario").textContent = usuario.username;
    document.getElementById("email-usuario").textContent = usuario.email;

    const fecha = new Date(usuario.fecha_creacion);
    const fechaFormateada = fecha.toLocaleDateString('es-AR');
    document.getElementById("fecha-usuario").textContent = fechaFormateada;

  } catch (error) {
    console.error("Error al obtener los datos del usuario:", error);
  }
}
cargarDatosUsuario();
























  }
});

























function checkLoginStatus() {
  const token = localStorage.getItem('token');
  if (token) {
    // Opcional: validar token con backend
    mostrarIconoUsuario();
  }
}

checkLoginStatus();