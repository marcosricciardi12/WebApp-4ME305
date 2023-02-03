import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth/auth.service';
import Swal from 'sweetalert2';


function delay(ms: number) {
  return new Promise( resolve => setTimeout(resolve, ms) );
}

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  loginForm!: FormGroup;

  constructor(
    private authService:AuthService,
    private formBuilder: FormBuilder,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.loginForm = this.formBuilder.group({
      user: ['', Validators.required],
      password: ['', Validators.required]
   });
  }


  login(dataLogin:any) {
    console.log('Checking Credentials...');
    this.authService.login(dataLogin).subscribe({
      next: async (rta) => {
        const Toast = Swal.mixin({
          toast: true,
          position: 'top-end',
          showConfirmButton: false,
          timer: 3000,
          timerProgressBar: true,
          didOpen: (toast) => {
            toast.addEventListener('mouseenter', Swal.stopTimer)
            toast.addEventListener('mouseleave', Swal.resumeTimer)
          }
        })
        
        Toast.fire({
          icon: 'success',
          title: 'Signed in successfully',
          footer: 'Redirecting'
        })
        await delay(2500);

        localStorage.setItem('token',rta.access_token);
        this.router.navigate(['/', 'home']);
      }, error: (error) =>{
        Swal.fire({
          icon: 'error',
          title: 'Oops...',
          text: 'Wrong credential! Try again'
        })
        console.log('error: ', error);
        localStorage.removeItem('token');
      }, complete: () => {
        console.log('Termino');
      }
    })
  }


  submit() {
    if (this.loginForm.valid) {
        console.log(this.loginForm.value);
        let user = this.loginForm.value.user;
        let password = this.loginForm.value.password;

        // console.log('Credenciales: ', {email, password});
        this.login({user, password});
      }
      else{
        alert("Invalid Form")
      }
    }  

}
