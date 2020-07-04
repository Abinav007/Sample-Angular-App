import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(private httpClient: HttpClient) { }
  Firstname = "User";
  Lastname = "Pass";
  get (url, params) {
    this.httpClient.post(url,params).toPromise().then(data => {
      console.log(data);
    })
  }
}
