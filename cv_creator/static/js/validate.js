function validate() {
  // elements
  const form = document.getElementById("form");
  const name = document.getElementById("name");
  const email = document.getElementById("email");
  const phone = document.getElementById("phone");
  const job = document.getElementById("job");
  const urls = document.getElementById("urls");
  const about = document.getElementById("about");
  const exp = document.getElementById("exp");
  const edu = document.getElementById("education");
  const lang = document.getElementById("lang");
  const top = document.getElementById("top");
  const soft = document.getElementById("soft")

  // email pattern
  const Regexemail = /[A-Z-a-z-0-9-.]@[a-z].[a-z-.]/;
  var msg = "";

  // check if empty
  if (
    name.value.length < 1 ||
    job.value.length < 1 ||
    phone.value.length < 1 ||
    about.value.length < 1 ||
    exp.value.length < 1 ||
    edu.value.length < 1 ||
    lang.value.length < 1 ||
    top.value.length < 1 ||
    soft.value.length < 1
  ) {
    msg = "Por favor rellena los campos faltantes";
    alert(msg);
  }
  // check email
  else if (!Regexemail.test(email.value)) {
    msg = "El correo no es valido";
    alert(msg);
  } else {
    form.submit()
  }
}
