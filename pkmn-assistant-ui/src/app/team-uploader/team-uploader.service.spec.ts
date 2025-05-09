import { TestBed } from '@angular/core/testing';

import { TeamUploaderService } from './team-uploader.service';

describe('TeamUploaderService', () => {
  let service: TeamUploaderService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(TeamUploaderService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
