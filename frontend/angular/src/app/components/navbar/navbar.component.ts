import { Component, OnInit } from '@angular/core';
import { AuthService } from 'src/app/services/auth/auth.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  token: any;
  admin = true;
  user:any = "";
  constructor(
    private authService:AuthService
  ) { }

  ngOnInit(): void {
    let token = localStorage.getItem("token") || "";
    if (token) {
      let decodedJWT = JSON.parse(window.atob(token.split('.')[1]));
      this.user = decodedJWT.user
    }

  }
  get isToken() {
    return localStorage.getItem('token') || undefined;
 }

  logout() {
    this.authService.logout();
  }

}
