import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { HttpHeaders } from '@angular/common/http';
import { Item } from './item.data';



@Injectable({
  providedIn: 'root'
})
export class TopItems {
  private baseUrl = 'http://127.0.0.1:5000';
  private apiUrl = `${this.baseUrl}/get-data/top-tracks`;

  constructor(private http: HttpClient) { }

  getTopItems(): Observable<Item[]> {
    return this.http.get<Item[]>(this.apiUrl, {withCredentials: true});
  }

  checkAuthStatus(): Observable<any> {
    return this.http.get(`${this.baseUrl}/auth/status`, { withCredentials: true });
  }

  login(): void {
    window.location.href = `${this.baseUrl}/auth/login`;
  }
}
