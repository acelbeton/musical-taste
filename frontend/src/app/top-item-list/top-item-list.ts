import { Component } from '@angular/core';
import { Item } from '../item.data';
import { TopItems } from '../top-items';

@Component({
  selector: 'app-top-item-list',
  imports: [],
  templateUrl: './top-item-list.html',
  styleUrl: './top-item-list.scss'
})
export class TopItemList {
  items: Item[] = [];
  isLoading = false;
  error: string | null = null;

  constructor(private itemService: TopItems) {}

  ngOnInit(): void {
    this.loadTopItems();
  }

  loadTopItems(): void {
    this.isLoading = true;
    this.error = null;

    this.itemService.getTopItems().subscribe({
      next: (data) => {
        console.log(data);
        this.items = data;
        this.isLoading = false;
      },
      error: (error) => {
        this.error = "Hiba történt";
        this.isLoading = false;
        console.error("Api hiba:", error);
      }
    })
  }
}
