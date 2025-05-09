// src/app/services/upload.service.ts
import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class TeamUploaderService {
  constructor(private http: HttpClient) {}

  analyzeTeam(file: File) {
    const form = new FormData();
    form.append('image', file);
    return this.http.post('/api/teams/analyze', form);
  }
}
