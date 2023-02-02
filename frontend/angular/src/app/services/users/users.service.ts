import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, take } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UsersService {
  url = 'users'
  url_i = 'user'

  constructor(private httpClient: HttpClient) { }

  getUser(id: any) {
    let auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    return  this.httpClient.get(this.url_i + "/" + id.toString(), {headers: headers});
  }

  createUser(dataRegistry: any): Observable<any> {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
    });
    return  this.httpClient.post(this.url, dataRegistry, {headers: headers}).pipe(take(1));;
  }

}
