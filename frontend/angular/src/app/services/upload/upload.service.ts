import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, take } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UploadService {
  url = 'users'

  constructor(private httpClient: HttpClient) { }

  upload_image(dataFile: any) {
    console.log(dataFile)
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${auth_token}`
    });
    this.httpClient.post('upload', dataFile, {headers: headers}).subscribe(response => {
    console.log(response);
  });
  }
}
