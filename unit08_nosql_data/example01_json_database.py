"""
範例 1：使用 JSON 作為簡單資料庫

這個範例展示如何使用 JSON 檔案來儲存和管理資料，
實現類似資料庫的基本功能（新增、查詢、更新、刪除）。

生活情境：
管理個人聯絡人資料，包含姓名、電話、email 等資訊。
"""

import json
import os
from datetime import datetime


class ContactManager:
    """聯絡人管理系統"""

    def __init__(self, filename="contacts.json"):
        """
        初始化聯絡人管理系統

        參數:
            filename: JSON 資料檔案名稱
        """
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        """載入聯絡人資料"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print(f"警告：{self.filename} 格式錯誤，建立新資料庫")
                return []
        else:
            return []

    def save_contacts(self):
        """儲存聯絡人資料"""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.contacts, f, ensure_ascii=False, indent=2)

    def add_contact(self, name, phone, email=""):
        """
        新增聯絡人

        參數:
            name: 姓名
            phone: 電話
            email: Email（選填）
        """
        contact = {
            "id": self.generate_id(),
            "name": name,
            "phone": phone,
            "email": email,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        self.contacts.append(contact)
        self.save_contacts()
        print(f"✓ 已新增聯絡人：{name}")
        return contact

    def generate_id(self):
        """生成唯一 ID"""
        if not self.contacts:
            return 1
        return max(c["id"] for c in self.contacts) + 1

    def get_all_contacts(self):
        """取得所有聯絡人"""
        return self.contacts

    def find_by_name(self, name):
        """
        依姓名查詢聯絡人

        參數:
            name: 要查詢的姓名（支援部分比對）
        """
        results = [c for c in self.contacts if name.lower() in c["name"].lower()]
        return results

    def find_by_id(self, contact_id):
        """
        依 ID 查詢聯絡人

        參數:
            contact_id: 聯絡人 ID
        """
        for contact in self.contacts:
            if contact["id"] == contact_id:
                return contact
        return None

    def update_contact(self, contact_id, name=None, phone=None, email=None):
        """
        更新聯絡人資料

        參數:
            contact_id: 聯絡人 ID
            name: 新姓名（選填）
            phone: 新電話（選填）
            email: 新 Email（選填）
        """
        contact = self.find_by_id(contact_id)

        if not contact:
            print(f"✗ 找不到 ID 為 {contact_id} 的聯絡人")
            return False

        if name:
            contact["name"] = name
        if phone:
            contact["phone"] = phone
        if email is not None:  # 允許設定空字串
            contact["email"] = email

        contact["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.save_contacts()
        print(f"✓ 已更新聯絡人 ID {contact_id}")
        return True

    def delete_contact(self, contact_id):
        """
        刪除聯絡人

        參數:
            contact_id: 聯絡人 ID
        """
        contact = self.find_by_id(contact_id)

        if not contact:
            print(f"✗ 找不到 ID 為 {contact_id} 的聯絡人")
            return False

        self.contacts.remove(contact)
        self.save_contacts()
        print(f"✓ 已刪除聯絡人：{contact['name']}")
        return True

    def display_contacts(self, contacts=None):
        """顯示聯絡人資訊"""
        if contacts is None:
            contacts = self.contacts

        if not contacts:
            print("目前沒有聯絡人資料")
            return

        print("\n" + "=" * 60)
        for contact in contacts:
            print(f"ID: {contact['id']}")
            print(f"姓名: {contact['name']}")
            print(f"電話: {contact['phone']}")
            print(f"Email: {contact.get('email', '(未設定)')}")
            print(f"建立時間: {contact['created_at']}")
            if "updated_at" in contact:
                print(f"更新時間: {contact['updated_at']}")
            print("-" * 60)


def main():
    """主程式"""
    print("JSON 資料庫範例：聯絡人管理系統")
    print("=" * 60)

    # 建立管理器
    manager = ContactManager()

    # 新增聯絡人
    print("\n【新增聯絡人】")
    manager.add_contact("王小明", "0912-345-678", "ming@example.com")
    manager.add_contact("李小華", "0923-456-789", "hua@example.com")
    manager.add_contact("張大同", "0934-567-890")

    # 顯示所有聯絡人
    print("\n【所有聯絡人】")
    manager.display_contacts()

    # 查詢聯絡人
    print("\n【查詢「小」的聯絡人】")
    results = manager.find_by_name("小")
    manager.display_contacts(results)

    # 更新聯絡人
    print("\n【更新聯絡人】")
    manager.update_contact(1, phone="0911-111-111")

    # 顯示更新後的聯絡人
    contact = manager.find_by_id(1)
    if contact:
        print(f"\n更新後的聯絡人資料：")
        manager.display_contacts([contact])

    # 刪除聯絡人
    print("\n【刪除聯絡人】")
    manager.delete_contact(2)

    # 顯示剩餘聯絡人
    print("\n【剩餘聯絡人】")
    manager.display_contacts()

    print(f"\n資料已儲存至：{manager.filename}")


if __name__ == "__main__":
    main()
