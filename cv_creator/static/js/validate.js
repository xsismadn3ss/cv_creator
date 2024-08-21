function validate() {
  // elements
  const form = document.getElementById("form");
  const title = document.getElementById("title");
  const phone = document.getElementById("phone");
  const job = document.getElementById("job");
  const urls = document.getElementById("urls");
  const about = document.getElementById("about");
  const exp = document.getElementById("exp");
  const edu = document.getElementById("education");
  const lang = document.getElementById("lang");
  const top = document.getElementById("top");
  const soft = document.getElementById("soft");

  // email pattern
  const Regexemail = /[A-Z-a-z-0-9-.]@[a-z].[a-z-.]/;
  var msg = "";

  // check if empty
  if (title.value.length < 1) {
    msg = "Agrega un titulo  tu CV";
    alert(msg);
  } else if (phone.value.length < 1) {
    msg = "Agrega un numero de teléfono";
    alert(msg);
  } else if (
    job.value.length < 1 ||
    about.value.length < 1 ||
    exp.value.length < 1 ||
    edu.value.length < 1
  ) {
    msg = "Por favor completa los campos de descripción"
    alert(msg)
  }
  else if (top.value.length < 1 || soft.value.length < 1 || lang.value.length < 1) {
    msg = "Por favor rellena el formulairo de habilidades"
    alert(msg)
  }
  else {
    form.submit();
  }
}
