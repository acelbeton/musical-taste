import { TestBed } from '@angular/core/testing';

import { TopItems } from './top-items';

describe('TopItems', () => {
  let service: TopItems;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(TopItems);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
