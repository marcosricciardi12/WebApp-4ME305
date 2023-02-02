import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { UsersService } from 'src/app/services/users/users.service';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  registerForm!: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private router: Router,
    private userService: UsersService
  ) { }

  ngOnInit(): void {
    this.registerForm = this.formBuilder.group({
      user: ['', Validators.required],
      password: ['', Validators.required],
      password2: ['', Validators.required],
      email: ['', [Validators.required, Validators.email, Validators.pattern('^[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$')]],
    })
  }

  register(dataLogin:any) {
    Swal.fire({
      title: 'Do you want to save the changes?',
      showDenyButton: true,
      showCancelButton: true,
      confirmButtonText: 'Save',
      denyButtonText: `Don't save`,
    }).then((result) => {
      /* Read more about isConfirmed, isDenied below */
      if (result.isConfirmed) {
        this.userService.createUser(dataLogin).subscribe({
          next: (rta) => {
            Swal.fire('Saved!', 'User ' + rta.user + ' ceated successfully', 'success')
            this.router.navigate(['/home']);
          }, error: (error) =>{
            Swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: 'Error creating user',
              footer: '<a href="">Why do I have this issue?</a>'
            })
            console.log('error: ', error);
          }, complete: () => {
            console.log('Termino');
          }
        })
      } else if (result.isDenied) {
        Swal.fire('Changes are not saved', '', 'info')
      }
    })
    
  }

  submit() {
    if (this.registerForm.valid) {
        console.log(this.registerForm.value);
        let user = this.registerForm.value.user;
        let password = this.registerForm.value.password;
        let password2 = this.registerForm.value.password2;
        let email = this.registerForm.value.email;
        // console.log('Credenciales: ', {email, password});
        if (password == password2){
          this.register({user, password, email});
        }
        else {
          Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Passwords do not mach!',
            footer: '<a href="">Why do I have this issue?</a>'
          })
        }
      }
      else{
        Swal.fire({
          icon: 'info',
          title: 'Oops...',
          text: 'Incomplete Form!',
          footer: '<a href="">Why do I have this issue?</a>'
        })
      }
    }  

}
