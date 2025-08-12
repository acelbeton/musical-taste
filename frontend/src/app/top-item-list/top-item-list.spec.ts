import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TopItemList } from './top-item-list';

describe('TopItemList', () => {
  let component: TopItemList;
  let fixture: ComponentFixture<TopItemList>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TopItemList]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TopItemList);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
