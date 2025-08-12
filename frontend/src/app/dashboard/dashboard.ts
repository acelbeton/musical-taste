import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { TopItemList } from '../top-item-list/top-item-list';


@Component({
  selector: 'app-dashboard',
  imports: [TopItemList],
  templateUrl: './dashboard.html',
  styleUrl: './dashboard.scss'
})
export class Dashboard {
  
}
