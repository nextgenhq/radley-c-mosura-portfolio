terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = "project-abcf14c5-b467-4586-839"
  region  = "us-central1"
}

# 1. Cloud Storage Bucket for Raw Lead Ingestion
resource "google_storage_bucket" "raw_leads_bucket" {
  name                     = "project-abcf14c5-raw-leads-bucket"
  location                 = "US"
  force_destroy            = true
  public_access_prevention = "enforced"

  uniform_bucket_level_access = true
}

# 2. BigQuery Dataset
resource "google_bigquery_dataset" "leads_analytics" {
  dataset_id                  = "leads_analytics"
  friendly_name               = "Leads Analytics Dataset"
  description                 = "Dataset containing raw and processed B2C lead records"
  location                    = "US"
  delete_contents_on_destroy = true
}

# 3. BigQuery Table Schema
resource "google_bigquery_table" "raw_leads" {
  dataset_id          = google_bigquery_dataset.leads_analytics.dataset_id
  table_id            = "raw_leads"
  deletion_protection = false

  schema = <<EOF
[
  {"name": "Business Name", "type": "STRING", "mode": "NULLABLE"},
  {"name": "Category", "type": "STRING", "mode": "NULLABLE"},
  {"name": "Rating", "type": "FLOAT", "mode": "NULLABLE"},
  {"name": "Review Count", "type": "INTEGER", "mode": "NULLABLE"},
  {"name": "Contact Phone", "type": "STRING", "mode": "NULLABLE"},
  {"name": "Website URL", "type": "STRING", "mode": "NULLABLE"},
  {"name": "Street Address", "type": "STRING", "mode": "NULLABLE"},
  {"name": "City", "type": "STRING", "mode": "NULLABLE"},
  {"name": "State", "type": "STRING", "mode": "NULLABLE"},
  {"name": "Zip Code", "type": "STRING", "mode": "NULLABLE"},
  {"name": "Latitude", "type": "FLOAT", "mode": "NULLABLE"},
  {"name": "Longitude", "type": "FLOAT", "mode": "NULLABLE"}
]
