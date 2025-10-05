import { TestBed } from '@angular/core/testing';
import { ContacServiceService } from './contac-service.service';

describe('ContacServiceService', () => {
  let service: ContacServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ContacServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
