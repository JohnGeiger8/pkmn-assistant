import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { RouterOutlet } from '@angular/router';
import { environment } from '../environments/environment';

@Component({
  selector: 'app-root',
  imports: [CommonModule, RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'pkmn-assistant';
  apiStatus: string = 'Loading...';
  errorMessage: string | null = null;

  private readonly http = inject(HttpClient);

  constructor() {
    this.http.get<{ status: string }>(`${environment.apiBaseUrl}/health`).subscribe({
      next: (response) => {
        this.apiStatus = response.status;
      },
      error: (error) => {
        this.apiStatus = 'Error';
        this.errorMessage = error?.message ?? 'Unable to reach backend.';
      }
    });
  }
}
