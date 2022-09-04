output "rds_hostname" {
  description = "RDS instance hostname"
  value       = aws_db_instance.pocpython.address
  sensitive   = true
}

output "rds_port" {
  description = "RDS instance port"
  value       = aws_db_instance.pocpython.port
  sensitive   = true
}

output "rds_username" {
  description = "RDS instance root username"
  value       = aws_db_instance.pocpython.username
  sensitive   = true
}

output "rds_replica_connection_parameters" {
  description = "RDS replica instance connection parameters"
  value       = "-h ${aws_db_instance.pocpython.address} -p ${aws_db_instance.pocpython.port} -U ${aws_db_instance.pocpython.username} postgres"
}
