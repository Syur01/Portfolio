import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root', // inyectado a nivel de app
})
export class ContacServiceService {
  private apiUrl = 'https://portfolio-pijl.onrender.com'; // URL real del backend

  constructor(private http: HttpClient) {}

  sendMessage(data: any): Observable<any> {
    return this.http.post(this.apiUrl, data);
  }
}
