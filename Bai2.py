atm_vault_balance = 50000000
user_account_balance = 10000000

def display_balances():
    """
    Tham số đầu vào: Không có
    Giá trị trả về: Không có
    """
    print("\n--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,.0f} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,.0f} VND")

def deposit_money(amount):
    """
    Tham số đầu vào: Số tiền muốn nạp (amount)
    Giá trị trả về: True nếu nạp thành công
    """
    global user_account_balance, atm_vault_balance
    user_account_balance += amount
    atm_vault_balance += amount

    print(f"Giao dịch thành công! Số dư tài khoản hiện tại: {user_account_balance:,.0f} VND.")
    return True

def check_withdrawal_rules(amount):
    """
    Tham số đầu vào: Số tiền cần rút (amount)
    Giá trị trả về: Trạng thái kiểm tra ("INSUFFICIENT_FUNDS", "ATM_OUT_OF_CASH", "OK")
    """
    if amount % 50000 != 0:
        return "INVALID_MULTIPLIER"
    if amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH"
    
    fee = 1100
    total_deduction = amount + fee

    if total_deduction > user_account_balance:
        return "INSUFFICIENT_FUNDS"
    
    return "OK"

def execute_withdrawal(total_deduction, amount_to_dispense):
    """
    Tham số đầu vào: Số tiền thực sự bị trừ (total_deduction), số tiền máy rút ra (amount_to_dispense)
    Giá trị trả về: Không có
    """
    global user_account_balance, atm_vault_balance
    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense

    print("Giao dịch đang xử lý...")
    print("Phí giao dịch: 1,100 VND")
    print(f"Bạn đã rút thành công {amount_to_dispense:,.0f} VND.")
    print(f"Số dư tài khoản còn lại: {user_account_balance:,.0f} VND.")

def main():
    """
    Tham số đầu vào: Không có
    Giá trị trả về: Không có
    """
    while True:
        print("\n============= SMART ATM =============")
        print("1. Xem số dư")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Kết thúc giao dịch")
        print("=====================================")
        choice = input("Vui lòng chọn giao dịch (1-4): ").strip()

        if choice == "1":
            display_balances()
        elif choice == "2":
            print("\n--- NẠP TIỀN ---")
            raw_amount = input("Nhập số tiền muốn nạp: ").strip()
            if not raw_amount.isdigit() or int(raw_amount) <= 0:
                print("Số tiền không hợp lệ")
            else:
                amount = int(raw_amount)
                deposit_money(amount)
        elif choice == "3":
            print("\n--- RÚT TIỀN ---")
            raw_amount = input("Nhập số tiền cần rút: ").strip()
            if not raw_amount.isdigit() or int(raw_amount) <= 0:
                print("Số tiền không hợp lệ")
            else:
                amount = int(raw_amount)

                status = check_withdrawal_rules(amount)
                if status == "INVALID_MULTIPLIER":
                    print("Số tiền rút phải là bội số của 50,000.")
                elif status == "ATM_OUT_OF_CASH":
                    print("Giao dịch thất bại: Máy ATM không đủ tiền mặt để phục vụ.")
                elif status == "INSUFFICIENT_FUNDS":
                    print("Giao dịch thất bại: Số dư tài khoản không đủ để thực hiện (bao gồm phí).")
                elif status == "OK":
                    fee = 1100
                    total_deduction = amount + fee
                    execute_withdrawal(total_deduction, amount)
        elif choice == "4":
            print("Cảm ơn quý khách đã sử dụng dịch vụ!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 4!")

if __name__ == "__main__":
    main()