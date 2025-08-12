import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Item } from './item.data';



@Injectable({
  providedIn: 'root'
})
export class TopItems {
  private apiUrl = 'http://localhost:5000/get-data/top-tracks';

  constructor(private http: HttpClient) { }

  getTopItems(): Observable<Item[]> {
    return this.http.get<Item[]>(this.apiUrl);
  }
}
