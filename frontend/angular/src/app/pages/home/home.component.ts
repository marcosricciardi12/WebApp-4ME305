import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { UploadService } from 'src/app/services/upload/upload.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  selectedFile!: File;
  url_redirect:any = "";
  message:any = "";

  constructor(
    private formBuilder: FormBuilder,
    private http: HttpClient,
    private router: Router,
    private uploadService: UploadService
  ) { }

  ngOnInit(): void {
    let token = localStorage.getItem("token") || "";
    if(token) {
      if (this.tokenExpired(token)) {
        localStorage.removeItem('token');
      }
    }
  }

  get isToken() {
    return localStorage.getItem('token') || undefined;
 }

 tokenExpired(token: string) {
  const expiry = (JSON.parse(atob(token.split('.')[1]))).exp;
  return (Math.floor((new Date).getTime() / 1000)) >= expiry;
}



onFileSelected(event: any) {
  this.selectedFile = event.target.files[0];
}

uploadImage() {
  const formData = new FormData();
  formData.append('image', this.selectedFile, this.selectedFile.name);
  this.uploadService.upload_image(formData).subscribe((data:any) =>{
    console.log('JSON data: ', data);
    this.url_redirect = data.url;
    this.message = data.message;
    window.location.href = this.url_redirect;
  });
  
} 

}
