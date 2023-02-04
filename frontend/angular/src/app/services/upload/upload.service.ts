import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, take } from 'rxjs';
import  { environment } from './../../../environments/environment';
@Injectable({
  providedIn: 'root'
})
export class UploadService {
  url = 'upload'

  constructor(private httpClient: HttpClient) { }

  upload_image(dataFile: any) {
    console.log(dataFile)
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${auth_token}`
    });
    this.httpClient.post((environment.url)+this.url, dataFile, {headers: headers}).subscribe(response => {
    console.log(response);
  });
  }
}
